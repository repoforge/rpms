# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Modifier

AutoProv:   0

Summary: Modify Email::MIME Objects Easily
Name: perl-Email-MIME-Modifier
Version: 1.441
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Modifier/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-Modifier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(Email::MIME::Modifier)

%description
Provides a number of useful methods for manipulating MIME messages.

These method are declared in the "Email::MIME" namespace, and are used
with "Email::MIME" objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
%{perl_vendorlib}/Email/MIME/Modifier.pm

%changelog
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.441-2
- Correctly provide perl(Email::MIME::Modifier).

* Sun Dec 10 2006 Dries Verachtert <dries@ulyssis.org> - 1.441-1
- Updated to release 1.441.
- Disabled automatic provides to make sure it doesn't provide perl(Email::MIME)
  anymore, thanks to Max Kanat-Alexander.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.42-1.2
- Rebuild for Fedora Core 5.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.42-1
- Initial package.

