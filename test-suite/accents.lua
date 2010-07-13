
local format, lower = string.format, string.lower

local alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local accents = {
    "hat", "check", "breve", "acute", "grave",
    "tilde", "bar", "vec", "dot", "ddot",
}
local styles = { }

if context then
    styles = { "it", "bi", "rm", "bf" }
else
    styles = { "it", "bfit", "rm", "bf" }
end

for c in alpha:gmatch"." do
    tex.sprint("$")
    for _,a in next, accents do
        for _,i in next, styles do
            tex.sprint(format("\\math%s{\\%s{%s}}", i, a, c))
            tex.sprint(format("\\math%s{\\%s{%s}}", i, a, lower(c)))
        end
    end
    tex.sprint("$\\par")
end
