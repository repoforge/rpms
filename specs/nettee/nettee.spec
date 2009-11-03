# $Id$
# Authority: dag
# Upstream: David Mathog <mathog$caltech,edu>

Summary: Network "tee" program
Name: nettee
Version: 0.1.9.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://saf.bio.caltech.edu/nettee.html

Source: http://saf.bio.caltech.edu/pub/software/linux_or_unix_tools/nettee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
nettee is a network "tee" program.  It can typically transfer
data between N nodes at (nearly) the full bandwidth provided by the switch
which connects them.  It is handy for cloning nodes or moving large
database files.

%prep
%setup

%build
%{__cc} %{optflags} -D_LARGEFILE64_SOURCE -o nettee nettee.c

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 nettee %{buildroot}%{_bindir}/nettee
%{__install} -D -m0644 nettee.1 %{buildroot}%{_mandir}/man1/nettee.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html *.sh *.TXT LICENSE
%doc %{_mandir}/man1/nettee.1*
%{_bindir}/nettee

%changelog
* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 0.1.9.1-1
- Updated to release 0.1.9.1.

* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 0.1.8-1
- Updated to release 0.1.8.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1
- Updated to release 0.1.7.

* Thu Jun 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.6-1
- Update to release 0.1.6.

* Tue May 10 2005 Dag Wieers <dag@wieers.com> - 0.1.5-1
- Initial package. (using DAR)
