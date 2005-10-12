# $Id$

# Authority: dries
# Upstream: Adam J. Foxson <afoxson$pobox,com>

%define real_name Net-IANA-PortNumbers
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Translate ports to services and vice versa
Name: perl-Net-IANA-PortNumbers
Version: 1.16
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IANA-PortNumbers/

Source: http://www.cpan.org/modules/by-module/Net/Net-IANA-PortNumbers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-libwww-perl

%description
With this module, you can translate ports to services and vice versa.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Net-IANA-PortNumbers/.packlist


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/IANA/PortNumbers.pm
%{perl_vendorlib}/Net/IANA

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.