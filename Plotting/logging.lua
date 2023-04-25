---@diagnostic disable: lowercase-global, undefined-global, undefined-field
--vscode bs

seperator="; "
vars = {'new', 'old'} -- list of variables to log
header="#; time"
for i=1, #vars do
  header=header..seperator..vars[i]
end
debug.log(header)

function log()
  local logstr = ""
  for i=1, #vars do
    logstr=logstr..seperator.._ENV[vars[i]]
  end
  debug.log(logstr)
end