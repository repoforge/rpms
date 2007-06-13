# $Id$
# Authority: dag
# Upstream: Chia-liang Kao (???) <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PerlIO-via-dynamic

Summary: Perl module that implements dynamic PerlIO layers
Name: perl-PerlIO-via-dynamic
Version: 0.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlIO-via-dynamic/

Source: http://www.cpan.org/modules/by-module/PerlIO/PerlIO-via-dynamic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
PerlIO-via-dynamic is a Perl module that implements dynamic PerlIO layers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/PerlIO::via::dynamic.3pm*
%dir %{perl_vendorlib}/PerlIO/
%dir %{perl_vendorlib}/PerlIO/via/
%{perl_vendorlib}/PerlIO/via/dynamic.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
