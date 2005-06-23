# $Id$
# Authority: dag
# Upstream: David Mathog <mathog@caltech.edu>

%define real_version 0.1.6

Summary: Network "tee" program
Name: nettee
Version: 0.1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://saf.bio.caltech.edu/nettee.html

Source: http://saf.bio.caltech.edu/pub/software/linux_or_unix_tools/nettee.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
nettee is a network "tee" program.  It can typically transfer
data between N nodes at (nearly) the full bandwidth provided by the switch
which connects them.  It is handy for cloning nodes or moving large
database files.

%prep
%setup -n %{name}-%{real_version}

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
%doc LICENSE *.TXT *.html *.sh
%doc %{_mandir}/man1/nettee.1*
%{_bindir}/nettee

%changelog
* Thu Jun 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.6-1
- Update to release 0.1.6.

* Tue May 10 2005 Dag Wieers <dag@wieers.com> - 0.1.5-1
- Initial package. (using DAR)
