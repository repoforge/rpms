# $Id: $

# Authority: dries
# Upstream: 

Summary: Superkaramba theme which displays your kotnet stats
Name: kotnet-limiet
Version: 0.1
Release: 1
License: GPL
Group: Applications/Graphics
URL: http://cernunos.studentenweb.org/kotnet-limiet.html

Source: http://cernunos.studentenweb.org/kotnet-limiet.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch: fedora.patch
Requires: superkaramba python

# Screenshot: http://cernunos.studentenweb.org/images/kotnet-limiet.png

%description
kotnet-limiet is a theme for superkaramba which displays your kotnet
download and upload stats, made by Stijn Opheide

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n kotnet-limiet
%patch -p 1

%build
# nothing to do

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/apps/kotnet-limiet
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -R kotnet-limiet.conf.template kotnet-limiet.theme pics $RPM_BUILD_ROOT/usr/share/apps/kotnet-limiet
cp kotnet-limiet knl.py $RPM_BUILD_ROOT/usr/bin
chmod a+x $RPM_BUILD_ROOT/usr/bin/kotnet-limiet

%files
%defattr(-,root,root,0755)
%doc README
%{_datadir}/apps/kotnet-limiet
%{_bindir}/knl.py
%{_bindir}/kotnet-limiet

%changelog
* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.1-1
- first packaging for Fedora Core 1
