# $Id$
# Authority: dries
# Upstream: Grant Grueninger <grantg$spamarrest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Myspace

Summary: Access MySpace.com from perl
Name: perl-WWW-Myspace
Version: 0.64
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Myspace/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Myspace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
WWW::Myspace.pm provides methods to access myspace.com accounts and functions
automatically. It provides a simple interface for scripts to log in,
access lists of friends, scan user's profiles, retreive profile
data, and post comments.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/add_friends*
%doc %{_mandir}/man1/approve_friends*
%doc %{_mandir}/man1/comment_myspace*
%doc %{_mandir}/man1/message_group*
%{_bindir}/add_friends
%{_bindir}/approve_friends
%{_bindir}/comment_myspace
%{_bindir}/message_group
%{perl_vendorlib}/WWW/Myspace.pm
%{perl_vendorlib}/WWW/Myspace/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Initial package.
