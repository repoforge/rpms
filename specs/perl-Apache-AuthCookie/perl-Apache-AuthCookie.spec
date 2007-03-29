# $Id$
# Authority: dries
# Upstream: Michael Schout <mschout$gkg,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-AuthCookie

Summary: Authentication and Authorization via cookie
Name: perl-Apache-AuthCookie
Version: 3.08
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-AuthCookie/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHOUT/Apache-AuthCookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, mod_perl >= 2.0

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
%makeinstall

### CLean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Apache*::AuthCookie.3pm*
%dir %{perl_vendorlib}/Apache*/
%{perl_vendorlib}/Apache*/AuthCookie.pm
%{perl_vendorlib}/Apache/AuthCookie/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 3.08-1
- Updated to release 3.08.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.06-1
- Initial package.
