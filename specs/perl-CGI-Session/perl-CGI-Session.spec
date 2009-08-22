# $Id$
# Authority: dries
# Upstream: Sherzod Ruzmetov <sherzodr$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Session

Summary: Persistent session data in CGI applications
Name: perl-CGI-Session
Version: 4.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Session/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(CGI) >= 3.26
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)


%description
CGI-Session is a Perl5 library that provides an easy, reliable and
modular session management system across HTTP requests. Persistency is a
key feature for such applications as shopping carts,
login/authentication routines, and application that need to carry data
accross HTTP requests. CGI::Session does that and many more.

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
%{__rm} -f %{buildroot}%{perl_vendorlib}/CGI/Session.pm.mine %{buildroot}%{perl_vendorlib}/CGI/Session.pm.r24[29]

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/CGI::Session.3pm*
%doc %{_mandir}/man3/CGI::Session::*.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Session/
%{perl_vendorlib}/CGI/Session.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 4.41-1
- Updated to version 4.41.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 4.38-1
- Updated to release 4.38.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 4.36-1
- Updated to release 4.36.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.32-1
- Updated to release 4.32.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 4.30-1
- Updated to release 4.30.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 4.20-1
- Updated to release 4.20.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 4.14-1
- Updated to release 4.14.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 4.13-1
- Updated to release 4.13.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.09-1
- Updated to release 4.09.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 4.03-1
- Updated to release 4.03.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.00_08-1
- Initial package.
