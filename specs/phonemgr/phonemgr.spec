# $Id$

# Authority: dag
# Upstream: <gnome-bluetooth$usefulinc,com>

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Phone manager
Name: phonemgr
Version: 0.2.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://usefulinc.com/software/phonemgr/

Source: http://usefulinc.com/software/phonemgr/releases/phonemgr-%{version}.tar.gz
Patch0: phonemgr-0.2.1-orbit2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomemm2-devel, libgnomeuimm2-devel, ORBit2-devel
#BuildRequires: gsmlib-devel, gnome-bluetooth

%description
A phone manager.

%prep
%setup
%patch -p0 -b .orbit2

%build
./autogen.sh
%configure \
	--disable-dependency-tracking \
	--disable-schemas-install
%{__make} %{?_smp_mflags} \
	ORBIT_IDL="%{_bindir}/orbit-idl-2"

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall \
	idldir="%{_datadir}/idl"
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/phonemgr/
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Cosmetic rebuild for Group-tag.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
