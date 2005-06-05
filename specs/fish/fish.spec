# $Id$
# Authority: dag

Summary: Friendly interactive shell
Name: fish
Version: 1.10.1
Release: 1
License: GPL
Group: System Environment/Shells
URL: http://roo.no-ip.org/fish/

Source: http://roo.no-ip.org/fish/files/%{version}/fish-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description 
fish is a shell geared towards interactive use. It's features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
#echo %{_bindir}/fish >>%{_sysconfdir}/shells

%files
%defattr(-, root, root, 0755)
%doc INSTALL README *.html doc_src/*.txt user_doc/html/
%doc %{_mandir}/man1/count.1*
%doc %{_mandir}/man1/fish.1*
%doc %{_mandir}/man1/mimedb.1*
%doc %{_mandir}/man1/set_color.1*
%doc %{_mandir}/man1/tokenize.1*
%doc %{_mandir}/man1/xsel.1x*
%config(noreplace) %{_sysconfdir}/fish
%config(noreplace) %{_sysconfdir}/fish_inputrc
%config(noreplace) %{_sysconfdir}/fish.d/
%{_bindir}/count
%{_bindir}/fish
%{_bindir}/mimedb
%{_bindir}/set_color
%{_bindir}/tokenize
%{_bindir}/xsel
%exclude %{_docdir}/fish

%changelog
* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 1.10.1-1
- Updated to release 1.0.1.

* Sat May 28 2005 Dag Wieers <dag@wieers.com> - 1.10-1
- Initial package. (using DAR)
