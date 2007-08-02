# $Id$
# Authority: dries
# Upstream: Sam Tregar <sam$tregar,com>

%define real_name HTML-Template
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: HTML Templates for CGI scripts
Name: perl-HTML-Template
Version: 2.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Template/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
With this module, you can use HTML templates in CGI scripts.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
        PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE Changes FAQ README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/Template.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.9-1
- Updated to release 2.9.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Initial package.
