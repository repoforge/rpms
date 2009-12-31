# $Id$
# Authority: cmr
# Upstream: Daisuke Murase <typester$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-AMF

Summary: serialize / deserialize AMF data
Name: perl-Data-AMF
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-AMF/

Source: http://search.cpan.org/CPAN/authors/id/T/TY/TYPESTER/Data-AMF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(DateTime)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Moose)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(YAML)
BuildRequires: perl >= 5.008001
Requires: perl(DateTime)
Requires: perl(Filter::Util::Call)
Requires: perl(Moose)
Requires: perl(Scalar::Util)
Requires: perl(UNIVERSAL::require)
Requires: perl(XML::LibXML)
Requires: perl >= 5.008001

%filter_from_requires /^perl*/d
%filter_setup


%description
This perl module is (de)serializer for Adobe's AMF (Action Message Format).
Data::AMF is core module and it recognize only AMF data, not AMF packet.
If you want to read/write AMF Packet, see Data::AMF::Packet instead.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Data::AMF.3pm*
%doc %{_mandir}/man3/Data::AMF::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/AMF/
%{perl_vendorlib}/Data/AMF.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Mon May 18 2009 Christoph Maser <cmr@financial.com> - 0.02004-2
- Add dependencies

* Tue May 12 2009 Christoph Maser <cmr@financial.com> - 0.02004-1
- Initial package. (using DAR)
