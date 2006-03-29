# $Id$
# Authority: dries
# Upstream: Sherzod Ruzmetov <sherzodr$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Session

Summary: Persistent session data in CGI applications
Name: perl-CGI-Session
Version: 4.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Session/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHERZODR/CGI-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Session.pm
%{perl_vendorlib}/CGI/Session

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.09-1
- Updated to release 4.09.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.03-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 4.03-1
- Updated to release 4.03.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.00_08-1
- Initial package.
