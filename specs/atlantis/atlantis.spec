# $Id$
# Authority: dag
# Upstream: Ali Akcaagac <aliakc$web,de>

Summary: Light-weight GNOME web browser
Name: atlantis
Version: 0.1.2
Release: 0
Group: Applications/Internet
License: Proprietary/Binary Only
URL: http://www.akcaagac.com/index_atlantis.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mirrors.egwn.net/cvsgnome/atlantis-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtkhtml2 >= 2.0

%description
Light-weight GNOME web browser.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}
tar -xvjf %{_builddir}/%{buildsubdir}/%{name}.tar.bz2 -C %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/atlantis/
%{_datadir}/applications/*.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/pixmaps/*

%changelog
* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.1.2-0
- Updated to release 0.1.2.

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Updated to release 0.1.1.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.1.0-0
- Initial package. (using DAR)
