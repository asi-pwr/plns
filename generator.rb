# encoding: utf-8
require 'yaml'
$data = YAML::load(File.read 'dane.yaml')

def find_rel a, b
    $data['Związki'].each do |name, rel|
        return name if rel == [a,b] or rel == [b,a]
    end
    nil
end

def pole name
    $data['Pola'][name]
end

def encja name
    $data['Tabele'][name]['encja']
end

def not_fk name, table
    not pole(name)['pk'] or pole(name)['pk'] == table
end

new_rels = {}
$data['Związki'].each do |name, rel|
    if new_rels.include? name.strip
        new_rels[name.strip][1] = rel[1]
    else
        new_rels[name] = rel.clone
    end
end
    if ARGV[0] == '10'
    locked_fields = {}
    $data['Tabele'].each do |name, table|
        locked_fields[name] = table['atrybuty'].reject {|a| not_fk a, table}
    end
    
    new_rels.each do |name, rel|
        puts "\n\\zwiazek\n\\encje"
        rel.each do |table|
            fields = $data['Tabele'][table]['atrybuty'].select{|a| not_fk(a, table)}.map{ |a| pole(a)['pk']?"\\pk{#{a}}": a }
            puts "    \\encja[#{encja(table).upcase}](" + fields.join(', ') + ")"
        end
        puts "\\relacje"
        if $data['Związki'][name] != rel # many-to-many
            rel << $data['Związki'][name][1]
        end
        rel.each do |table|
            locked_fields[table].reject! {|f| rel.include? pole(f)['pk']} 
            fields = $data['Tabele'][table]['atrybuty'].reject{|a| locked_fields[table].include? a}\
                                                       .map{ |a| pole(a)['pk']?pole(a)['pk'] == table ?"\\pk{#{a}}":"\\fk{#{a}}": a }
            puts "    \\relacja{#{table}}(" + fields.join(', ') + ")"
        end
    end
end

if ARGV[0] == '11'
    $data['Tabele'].each do |name, table|
        rels = []
        table['atrybuty'].each do |attr|
            if pole(attr).include? 'pk' and pole(attr)['pk'] != name
                rels << find_rel(name, pole(attr)['pk'])
            end
        end
        if rels.empty?
            rels = name
        elsif rels.length == 1
            rels = rels[0] + ',' + $data['Związki'][rels[0]].map {|e| encja(e)}.join(',')
        else
            rels = rels[0] + ',' + rels.map {|rel| encja($data['Związki'][rel].select {|e| e != name }[0])}.join(',')
        end
        puts "\\begin{relacja}{#{name}}{#{rels}}"
        puts "\\begin{schemat}"
        table['atrybuty'].each do |attr|
            field = pole(attr)
            fname = field['nazwa'] || attr
            domain = field['typ']
            mask = field['maska']
            obl = field['flagi'] =~ /opc/ ? '-' : '+'
            default = field['domyślnie'] || field['flagi'] =~ /opc/ ? field['typ'] == 'DateTime' ? 'NOW()' : ",,''" : '' 
            constraints = field['ograniczenia'] && field['ograniczenia'].join('\\newline').gsub(/([<>])/, "\\verb+\\1+")
            unique = (field['pk'] == name || field['flagi'] =~ /uniq/) ? '+' : '-'
            key = field['pk'] ? field['pk'] == name ? 'PK' : 'FK' : ''
            refs = field['pk'] != name ? field['pk'] : ''
            source = (!default.empty? || field['pk']) ? 'SZBD' : 'USER'
            puts "#{fname} & #{domain} & #{mask} & #{obl} & #{default} & #{constraints} & #{unique} & #{key} & #{refs} & #{source} \\\\"
        end
        puts "\\end{schemat}"
        puts "\\begin{atrybuty}"
        table['atrybuty'].each do |attr|
            field = pole(attr)
            fname = field['nazwa'] || attr
            puts "#{fname} & #{field['opis']} \\\\"
        end
        puts "\\end{atrybuty}"
        cols = table['atrybuty'].map{|a|'|' + (pole(a)['typ'] == 'Int+' ? 'c':'Y')}.join
        cols.sub!(/c$/,'Y') unless cols.include? 'Y'
        puts "\\begin{przyklady}\\begin{tabularx}{\\textwidth}{" + cols + "|}\\hline"
        puts table['atrybuty'].map{|a| "\\begin{sideways}#{pole(a)['nazwa'] || a}\\end{sideways}"}.join('&') + '\\\\\\hline'
        table['przykłady'].each do |example|
            puts example.join(' & ') + '\\\\'
        end
        puts "\\hline\\end{tabularx}\\end{przyklady}"
        puts "\\end{relacja}\n"
    end
end

if ARGV[0] == '12'
    tables = {}
    new_rels.each do |name, rel|
        if $data['Związki'][name] != rel # many-to-many
            rel << $data['Związki'][name][1]
        end
        rel.each do |table|
            fields = $data['Tabele'][table]['atrybuty'].map{ |a| pole(a)['pk']?pole(a)['pk'] == table ?"\\pk{#{a}}":"\\fk{#{a}}": a }
            tables[table] =  "    \\relacja{#{table}}(" + fields.join(', ') + ")"
        end
    end
    puts "\\begin{relacje}\n" + tables.values.join("\n") + "\n\\end{relacje}\n"
    puts "\\begin{atrybuty}"
    i = 0
    $data['Pola'].each do |name, attr|
        next if attr['nazwa']
        tables = $data['Tabele'].select{|n, tbl| tbl['atrybuty'].map {|a| pole(a)['nazwa'] || a}.include? name}.map(&:first)
        puts "#{name} & #{attr['typ']} & " + tables.join('\\newline ') + " \\\\\\hline"
        i += 1
        if i == 20 
            puts "\\end{atrybuty}"
            puts "\\begin{atrybuty}"
        end
    end
    puts "\\end{atrybuty}"
end

if ARGV[0] == '13'
    $data['Perspektywy'].each do |name,view|
        puts "\\subsection{#{name}}"
        puts "Użytkownicy: " + view['Userzy'].join(', ')
        puts "\nTransakcje: " + view['Transakcje'].map{|t| "\\ref{TRA:#{t['Nazwa']}}"}.join(', ')
        view['Transakcje'].each do |tra|
            puts "\\subsubsection*{\\ref{TRA:#{tra['Nazwa']}} #{tra['Nazwa']}}"
            puts "\\begin{tabularx}{\\textwidth}{|Y|Y|Y|Y|Y|}\\hline"
            puts "Relacja & Pole & Zapis & Odczyt & Modyfikacja \\\\\\hline"
            fields = {}
            tra['Pola'].each.with_index do |type, idx|
                if type == '*'
                    type = tra['Tabele'].map{|t| $data['Tabele'][t]['atrybuty']}.flatten
                end
                type.each do |field|
                    fs = []
                    if field =~ /(.*?)\.\*/
                        fs += $data['Tabele'][$1]['atrybuty'].map {|a| [$1, pole(a)['nazwa'] || a] }
                    elsif field =~ /(.*?)\.(.*)/
                        fs << [$1, pole($2)['nazwa'] || $2]
                    else
                        tra['Tabele'].each do |tbl|
                            fs << [tbl, pole(field)['nazwa'] || field] if $data['Tabele'][tbl]['atrybuty'].include? field
                        end
                    end
                    fs.each { |f| fields[f] ||= [false, false, false]; fields[f][idx] = true }
                end
            end
            fields.each do |field, types|
                puts field.join(' & ') + ' & ' + types.map{|t| t ?'+':''}.join(' & ') + '\\\\'
            end
            puts "\\hline\\end{tabularx}"
        end
    end
end
