# $Id$
# Authority: dag

Summary: Navigate cd
Name: cdargs
Version: 1.31 
Release: 1
License: GPL
Group: Applications/File
URL: http://www.skamphausen.de/software/cdargs/

Source: http://www.skamphausen.de/software/cdargs/cdargs-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Navigate cd Arguments/expand the shell built-in cd with bookmarks and browser

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc contrib/cdargs-bash.sh contrib/cdargs-tcsh.csh contrib/cdargs.el
%doc %{_mandir}/man1/cdargs.1*
%{_bindir}/cdargs

%clean
%{__rm} -rf %{buildroot}

%changelog
* Tue Sep 20 2005 Dag Wieers <dag@wieers.com> - 1.31-1
- Initial package. (using DAR)
