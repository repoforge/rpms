# $Id$
# Authority: dag
# Upstream: Muli Ben-Yehuda <mulix$mulix,org>

# ExcludeDist: fc2 fc3

# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/debug/syscalltrack
%define modules_orig module/rules/sct_rules.o module/hijack/sct_hijack.o
%define modules sct_rules.o sct_hijack.o

Summary: Track invocations of system calls across your Linux system
Name: syscalltrack
Version: 0.82
Release: 2%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://syscalltrack.sourceforge.net/

Source: http://dl.sf.net/syscalltrack/syscalltrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source >= 2.4
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

%description
Syscalltrack allows you - the 'root' user - to track invocations of system
calls across your Linux system. You specify rules that specify which system
call invocations will be tracked, and what to do when a rule matches a
system call invocation. You can log the system call invocation, fail it (i.e.
force it to return some error code), or suspend the process executing it (e.g.
so you could attach a debugger to the process at that point, or so you could
find who is the parent process of that process, etc.). You could even kill the
process, if you were feeling particularly sadistic.

%package -n kernel-module-%{name}
Summary: Kernel modules for %{name}
Group: System Environment/Kernel
Release: %{release}_%{kversion}_%{krelease}%{?dist}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules

%description -n kernel-module-%{name}
Kernel modules for %{name}.

%prep
%setup -n %{name}-%{version}

%build
### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
./configure \
	--with-linux="%{_usrsrc}/linux-%{kversion}-%{krelease}" \
	--with-module-dir="%{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}" \
	--prefix="%{buildroot}%{_prefix}" \
	--libdir="%{buildroot}%{_libdir}" \
	--bindir="%{buildroot}%{_bindir}" \
	--mandir="%{buildroot}%{_mandir}/man1"
%{__make} %{?_smp_mflags}
%{__install} -d -m0755 %{name}-up/
%{__mv} -f %{modules_orig} %{name}-up/

### Prepare SMP kernel.
#cd %{_usrsrc}/linux-%{kversion}-%{krelease}
#%{__make} -s distclean &>/dev/null
#%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
#%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
#cd -

### Make SMP module.
#%{__make} clean INCLUDEDIR="%{_libdir}/%{kversion}-%{krelease}smp/build/include" all
#%{__install} -d -m0755 %{name}-smp/
#%{__mv} -f %{modules_orig} %{name}-smp/

%install
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1
%makeinstall MANDIR="%{buildroot}%{_mandir}/man1/"

### Install UP module.
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd %{name}-up/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Install SMP module.
#%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
#cd %{name}-smp/
#%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
#cd -

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README RUNNING TODO doc/*.html doc/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/%{name}-%{version}/

%files -n kernel-module-syscalltrack
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
#%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Fri Mar 21 2003 Dag Wieers <dag@wieers.com> - 0.82-1
- Renamed subpackage to "kernel-module-syscalltrack".

* Tue Mar 18 2003 Dag Wieers <dag@wieers.com> - 0.82-0
- Initial package. (using DAR)
