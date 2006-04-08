# $Id$
# Authority: dries

Summary: Fantasy MMORPG server suing AI/A-Life techniques
Name: cyphesis
Version: 0.5.6
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://www.worldforge.org/wf/dev/eng/servers/cyphesis

Source: http://dl.sf.net/worldforge/cyphesis-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: varconf-devel >= 0.6.4, atlas-c++-devel, mercator-devel, skstream-devel
BuildRequires: postgresql-devel, python-devel, readline-devel, gcc-c++
BuildRequires: libsigc++-devel, wfmath-devel, libgcrypt-devel

%description
Cyphesis is a fantasy MMORPG server (and NPC engine for servers) using
AI/A-Life techniques which doesn't have a predefined story. It is the
Artificial Intelligence and Artificial Life server/client used by the
WorldForge project.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/cy*
%dir %{_sysconfdir}/cyphesis/
%config(noreplace) %{_sysconfdir}/cyphesis/*.xml
%config(noreplace) %{_sysconfdir}/cyphesis/*.vconf
%{_bindir}/cydumprules
%{_bindir}/cyclient
%{_bindir}/cyconvertrules
%{_bindir}/cypasswd
%{_bindir}/cyphesis
%{_bindir}/cyloadrules
%{_bindir}/cyaddrules
%{_bindir}/cyconfig
%{_bindir}/cycmd
%{_datadir}/cyphesis/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.6-1.2
- Rebuild for Fedora Core 5.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.6-1
- Updated to release 0.5.6.

* Sun Dec 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.5-1
- Updated to release 0.5.5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1
- Initial package.
