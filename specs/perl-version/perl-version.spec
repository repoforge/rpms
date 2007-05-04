# $Id$
# Authority: dag
# Upstream: John Peacock <jpeacock$rowman,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name version
%define real_version  0.7203

Summary: Perl module that implements for Version Objects
Name: perl-version
Version: 0.72.3
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/version/

Source: http://www.cpan.org/modules/by-module/version/version-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
version is a Perl module that implements for Version Objects.

%prep
%setup -n %{real_name}-%{real_version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/version.3pm*
%{perl_vendorarch}/version.pm
%{perl_vendorarch}/version.pod
%{perl_vendorarch}/version/
%{perl_vendorarch}/auto/version/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.72.3-1
- Initial package. (using DAR)
