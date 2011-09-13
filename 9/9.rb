(1..1000).each do |i|
  (i..1000).each do |j|
    (j..1000).each do |k|
      next if i + j + k > 1000
      next if k * k > i * i + j * j

      if i * i + j * j == k * k
        if i + j + k == 1000
          puts "#{i} * #{j} * #{k} = #{i * j * k}"
          exit
        end
      end
    end
  end
end