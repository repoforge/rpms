# $Id$

# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define real_name Email-MIME-Modifier
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Modify Email::MIME Objects Easily
Name: perl-Email-MIME-Modifier
Version: 1.42
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Modifier/

Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/Email-MIME-Modifier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Provides a number of useful methods for manipulating MIME messages.

These method are declared in the "Email::MIME" namespace, and are used
with "Email::MIME" objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Email/MIME/Modifier.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.42-1
- Initial package.

