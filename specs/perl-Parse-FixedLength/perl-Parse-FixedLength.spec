# $Id$

# Authority: dries
# Upstream: Douglas Wilson <dougw$cpan,org>

%define real_name Parse-FixedLength
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Parse an ascii string containing fixed length fields into component parts
Name: perl-Parse-FixedLength
Version: 5.33
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-FixedLength/

Source: http://search.cpan.org/CPAN/authors/id/D/DO/DOUGW/Parse-FixedLength-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parse an ascii string containing fixed length fields into component parts.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Parse/FixedLength.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 5.33-1
- Initial package.
