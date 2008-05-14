# $Id$
# Authority: dries
# Upstream: Grant Grueninger <grantg$spamarrest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Myspace

Summary: Access MySpace.com from perl
Name: perl-WWW-Myspace
Version: 0.79
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

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
#%doc %{_mandir}/man1/add_friends.1*
%doc %{_mandir}/man1/approve_friends.1*
%doc %{_mandir}/man1/comment_myspace.1*
%doc %{_mandir}/man1/message_group.1*
%doc %{_mandir}/man3/WWW::Myspace.3pm*
%doc %{_mandir}/man3/WWW::Myspace::*.3pm*
#%{_bindir}/add_friends
%{_bindir}/approve_friends
%{_bindir}/comment_myspace
%{_bindir}/message_group
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Myspace/
%{perl_vendorlib}/WWW/Myspace.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to release 0.79.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.75-1
- Updated to release 0.75.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.74-1
- Updated to release 0.74.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.73-1
- Updated to release 0.73.

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
