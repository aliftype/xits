
local format, lower = string.format, string.lower

local alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local styles = { }

if context then
    styles = { "it", "bi", "rm", "bf" }
else
    styles = { "it", "bfit", "rm", "bf" }
end

for c in alpha:gmatch"." do
    tex.sprint("$")
    for _,i in next, styles do
        tex.sprint(format("\\math%s{%s^1_1}\\kern5pt", i, c))
        tex.sprint(format("\\math%s{%s^1_1}\\kern5pt", i, lower(c)))
    end
    tex.sprint("$\\blank[big]")
end
