
if confget("RPM::Upgrade-Virtual/b", "false") == "false" then
    return
end

knames = { "hugemem", "bigmem", "enterprise", "smp", "BOOT" }

-- get kernel package name for running kernel (kernel-smp, kernel, etc)
function get_kerneltype()
	for i, ktype in ipairs(knames) do
		if string.find(posix.uname("%r"), ktype) then
			return ktype
		end
	end
	-- it's either unknown type or normal UP system
	return ""
end

-- get package name
function get_kernelname()
	suffix = get_kerneltype()
	if suffix == "" then
		return "kernel"
	else
		return "kernel-"..suffix
	end
end

-- if grubby is available set default kernel to version
function set_default(version)
	if not posix.access('/sbin/grubby', 'x') then
		return
	end
	grubby = io.popen("LANG=C /sbin/grubby --default-kernel")
	for line in grubby.lines(grubby) do
		-- don't touch the default if it's not a linux system
		if string.find(line, "vmlinuz") then
			ktype = get_kerneltype()
			vmlinuz = '/boot/vmlinuz-'..version..ktype
			if posix.access(vmlinuz, 'f') then
				print(_("Setting "..vmlinuz.." as new default kernel."))
				os.execute('/sbin/grubby --set-default='..vmlinuz)
			else
				aptwarning(_("Unable to set new default kernel "..vmlinuz))
			end
		end
	end
end

-- find + mark for install any packages where uname -r is part of pkg name
-- eg external kernel modules
function upgrade_kernel_modules(new_version)
    modprefix = confgetlist("Kernel::Module-Prefix")
	if not new_version or not modprefix then
		return
	end

	seenpkgs = {}
	pkgs = pkglist()
	for i, pkg in ipairs(pkgs) do
		-- oh fun.. loop through all installed packages and see there are
		-- any which provide module-prefix, try to install version matching
		-- our new kernel
    	if not pkgisvirtual(pkg) and pkgvercur(pkg) then
        	ver = pkgvercur(pkg)
        	for j, prov in ipairs(verprovlist(ver)) do
				for x, prefix in ipairs(modprefix) do
            		if string.sub(prov.name, 1, string.len(prefix)) == prefix then
						inst = pkgfind(prov.name.."-"..new_version)
						if inst then
							markinstall(inst)
						elseif not seenpkgs[prov.name] == true then
							print(_("WARNING: "..prov.name.." not available for kernel "..new_version.."!"))
                    	end                                         
						seenpkgs[prov.name] = true
					end
            	end
        	end
    	end
	end
end


-- find all virtualized packages, their versions and if they're installed
function find_instonly_pkgs()
	pkgs = {}
	for i, pkg in ipairs(pkglist()) do
		idx = string.find(pkgname(pkg), "#")
		ver = pkgvercur(pkg)
		if idx and not pkgisvirtual(pkg) then
			name = string.sub(pkgname(pkg), 1, idx-1)
			if not ver then
				ver = pkgvercand(pkg)
			end
			-- new entry
			if not pkgs[name] then
				tmp = {}
				tmp.pkg = pkg
				tmp.ver = ver
				tmp.inst = false
				pkgs[name] = tmp
			end
			if pkgvercur(pkg) then
				pkgs[name].inst = true
			end
			-- mark it as latest if newer than what already known
			if ver and verstrcmp(verstr(ver), verstr(pkgs[name].ver)) > 0 then
				pkgs[name].ver = ver
				pkgs[name].pkg = pkg
			end
		end
	end
	return pkgs
end

-- mark installed virtualized packages for "upgrade"
function mark_upgrade(name, pkg)
	kname = get_kernelname()
	if pkg.inst and not pkgvercur(pkg.pkg) then
		markinstall(pkg.pkg)
		if name == kname and not pkgvercur(pkg.pkg) then
			confset('Kernel::New-Version', verstr(pkg.ver))
		end
	end
end

-- find the latest version of given virtual pkg for installation
function mark_install(virtualpkg)
	kname = get_kernelname()
	pkgs = find_instonly_pkgs()
	for name in pkgs do
		if name == virtualpkg then
			selected = pkgs[name].pkg
		end
	end
	if virtualpkg == kname and not pkgvercur(pkgs[virtualpkg].pkg) then
		confset('Kernel::New-Version', verstr(pkgs[virtualpkg].ver))
	end
end

-- normal install operation
if script_slot == 'Scripts::AptGet::Install::SelectPackage' then
	modprefix = confgetlist('Kernel::Module-Prefix')
	for i, prefix in ipairs(modprefix) do
		if string.find(virtualname, prefix, 1, true) then
			moduname = virtualname.."-"..posix.uname("%r")
			modpkg = pkgfind(moduname)
			if modpkg then
				selected = modpkg
			else
				apterror(_("Couldn't find package "..moduname))
				return
			end
		end
	end
	mark_install(virtualname)
	return
elseif script_slot == 'Scripts::AptGet::Install::PreResolve' then
	kname = get_kernelname()
	if not confexists('Kernel::New-Version') then
		for i, pkg in ipairs(pkglist()) do
			idx = string.find(pkgname(pkg), "#")
			if statinstall(pkg) and idx then
				name = string.sub(pkgname(pkg), 1, idx-1)
				if kname == name and not pkgvercur(pkg) then
					confset('Kernel::New-Version', verstr(pkgvercand(pkg)))
				end
			end
		end	
	end
	if confexists('Kernel::New-Version') then
		upgrade_kernel_modules(confget('Kernel::New-Version'))
	end
-- if there's no virtual provide without the version in the name
-- we need to match it here instead of selectpackage
elseif script_slot == 'Scripts::AptGet::Install::TranslateArg' then
    modprefix = confgetlist('Kernel::Module-Prefix')
    for i, prefix in ipairs(modprefix) do
		if string.find(argument, prefix, 1, true) then
			translated = argument.."-"..posix.uname("%r")
		end
	end
	return
elseif script_slot == 'Scripts::AptGet::Upgrade' or 
   script_slot == 'Scripts::AptGet::DistUpgrade' then
	pkgs = find_instonly_pkgs()
	table.foreach(pkgs, mark_upgrade)
	if confexists('Kernel::New-Version') then
		upgrade_kernel_modules(confget('Kernel::New-Version'))
	end
elseif script_slot == 'Scripts::PM::Post' then
	if confget('Kernel::Set-Default/b', "false") == "true" and 
       confexists('Kernel::New-Version') then
		set_default(confget('Kernel::New-Version'))
	end
end
		
-- vim:ts=4:sw=4
