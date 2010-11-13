# $Id$
# Authority: dries

# Screenshot: http://cernunos.studentenweb.org/images/kotnet-limiet.png

Summary: Superkaramba theme which displays your kotnet stats
Name: kotnet-limiet
Version: 0.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://cernunos.studentenweb.org/kotnet-limiet.html

Source: http://cernunos.studentenweb.org/kotnet-limiet.tar.gz
Patch0: fedora.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: superkaramba, python

%description
kotnet-limiet is a theme for superkaramba which displays your kotnet
download and upload stats, made by Stijn Opheide

%prep
%setup -n kotnet-limiet
%patch0 -p1

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__mkdir_p} %{buildroot}%{_datadir}/apps/kotnet-limiet/
%{__cp} -ap kotnet-limiet.conf.template kotnet-limiet.theme pics \
    %{buildroot}%{_datadir}/apps/kotnet-limiet/
%{__install} -p -m0755 kotnet-limiet knl.py %{buildroot}%{_bindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/knl.py
%{_bindir}/kotnet-limiet
%{_datadir}/apps/kotnet-limiet

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.1-1
- first packaging for Fedora Core 1

