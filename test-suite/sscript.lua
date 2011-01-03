local format, lower = string.format, string.lower

local alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
local styles = { "it", "bi", "rm", "bf" }

for c in alpha:gmatch"." do
    for _,i in next, styles do
        context.mathematics(format([[\math%s{%s^1_1}\kern5pt]], i, c))
        context.mathematics(format([[\math%s{%s^1_1}\kern5pt]], i, lower(c)))
    end
    context.blank({"big"})
end
