# $Id$

# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define real_name Email-Address
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: RFC 2822 Address Parsing and Creation
Name: perl-Email-Address
Version: 1.80
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Address/

Source: http://search.cpan.org/CPAN/authors/id/C/CW/CWEST/Email-Address-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of "Email::Address" objects
found. Alternatley you may construct objects manually. The goal of this
software is to be correct, and very very fast.

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
%{perl_vendorlib}/Email/Address.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Initial package.

