# $Id$
# Authority: dries
# Upstream: Marc O. Gloor <mgloor$fhzv,ch>

# Screenshot: http://pubwww.fhzh.ch/~mgloor/data/screenie.jpg

Summary: Small frontend for screen
Name: screenie
Version: 1.12
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://pubwww.fhzh.ch/~mgloor/screenie.html

Source: http://pubwww.fhzv.ch/~mgloor/data/screenie.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Screenie is a small and lightweight screen frontend that is 
designed to be a session handler that simplifies the process 
of administrating detached jobs by providing an interactive 
menu.

%prep
gunzip -c %{SOURCE0} > /tmp/screenie

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 /tmp/screenie %{buildroot}%{_bindir}/screenie

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/screenie

%changelog
* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
