# $Id$
# Authority: shuff
# Upstream: <modules-interest$lists,sourceforge,net>

### EL6 ships with environment-modules-3.2.7b-6.el6
%{?el6:# Tag: rfx}

%define real_name modules
%define real_version 3.2.8

Summary: Dynamic modification of a user's environment
Name: environment-modules
Version: %{real_version}a
Release: 2%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://modules.sourceforge.net/

Source: http://downloads.sourceforge.net/project/modules/Modules/modules-%{real_version}/modules-%{version}.tar.gz
Source1: modules.sh
Source2: createmodule.sh
Patch0: environment-modules-3.2.7-bindir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: make
BuildRequires: man
BuildRequires: tcl-devel
BuildRequires: tclx-devel
Requires: procps

%description
The Environment Modules package provides for the dynamic modification of a
user's environment via modulefiles.

Each modulefile contains the information needed to configure the shell for an
application. Once the Modules package is initialized, the environment can be
modified on a per-module basis using the module command which interprets
modulefiles. Typically modulefiles instruct the module command to alter or set
shell environment variables such as PATH, MANPATH, etc. modulefiles may be
shared by many users on a system and users may have their own collection to
supplement or replace the shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an clean
fashion. All popular shells are supported, including bash, ksh, zsh, sh, csh,
tcsh, as well as some scripting languages such as perl.

Modules are useful in managing different versions of applications. Modules can
also be bundled into metamodules that will load an entire suite of different
applications. 

%prep
%setup -n %{real_name}-%{real_version}
%patch0 -p1 -b .bindir

%build
export CPPFLAGS=-DMANPATH=\'\"`manpath`\"\'
%configure \
    --disable-versioning \
    --prefix=%{_datadir} \
    --exec-prefix=%{_datadir}/Modules \
    --with-module-path=%{_sysconfdir}/modulefiles

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/profile.d
%{__install} -m0755 %SOURCE1 %{buildroot}%{_sysconfdir}/profile.d/modules.sh
%{__ln_s} %{_datadir}/Modules/init/csh %{buildroot}%{_sysconfdir}/profile.d/modules.csh
%{__install} -m0755 %SOURCE2 %{buildroot}%{_datadir}/Modules/bin
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/modulefiles

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.GPL README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/Modules/
%config(noreplace) %{_datadir}/Modules/init/.modulespath
%{_sysconfdir}/profile.d/*
%dir %{_sysconfdir}/modulefiles

%changelog
* Fri Apr 22 2011 Steve Huff <shuff@vecna.org> - 3.2.8a-2
- Marked .modulepath file as %config(noreplace) (thanks, Dr. Paul Cochrane!)

* Wed Apr 13 2011 Steve Huff <shuff@vecna.org> - 3.2.8a-1
- Initial package (ported from EPEL).
