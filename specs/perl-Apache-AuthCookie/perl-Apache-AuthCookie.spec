# $Id$
# Authority: dries
# Upstream: Michael Schout <mschout$gkg,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-AuthCookie

Summary: Authentication and Authorization via cookie
Name: perl-Apache-AuthCookie
Version: 3.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-AuthCookie/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-AuthCookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: mod_perl >= 2.0

%description
Apache::AuthCookie allows you to intercept a user's first unauthenticated
access to a protected document. The user will be presented with a custom
form where they can enter authentication credentials. The credentials are
posted to the server where AuthCookie verifies them and returns a session
key.

The session key is returned to the user's browser as a cookie. As a cookie,
the browser will pass the session key on every subsequent accesses.
AuthCookie will verify the session key and re-authenticate the user.


%prep
%setup -n %{real_name}-%{version}

%build
# -apxs /usr/sbin/apxs
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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.modperl2
%doc %{_mandir}/man3/Apache::AuthCookie.3pm*
%doc %{_mandir}/man3/Apache2::AuthCookie.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/AuthCookie/
%{perl_vendorlib}/Apache/AuthCookie.pm
%dir %{perl_vendorlib}/Apache2/
%{perl_vendorlib}/Apache2/AuthCookie.pm

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 3.12-1
- Updated to release 3.12.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 3.11-1
- Updated to release 3.11.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 3.08-1
- Updated to release 3.08.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.06-1
- Initial package.
