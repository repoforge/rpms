# $Id$
# Authority: cmr
# Upstream: Daisuke Murase <typester$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-AMF

Summary: serialize / deserialize AMF data
Name: perl-Data-AMF
Version: 0.02004
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-AMF/

Source: http://www.cpan.org/modules/by-module/Data/Data-AMF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.008001
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML)
Requires: perl >= 4:5.008001

%description
This perl module is (de)serializer for Adobe's AMF (Action Message Format). Data::AMF is core module and it recognize only AMF data, not AMF packet. If you want to read/write AMF Packet, see Data::AMF::Packet instead.

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
%doc %{_mandir}/man3/Data::AMF::Formatter.3pm*
%doc %{_mandir}/man3/Data::AMF::Formatter::AMF0.3pm*
%doc %{_mandir}/man3/Data::AMF::Header.3pm*
%doc %{_mandir}/man3/Data::AMF::IO.3pm*
%doc %{_mandir}/man3/Data::AMF::Message.3pm*
%doc %{_mandir}/man3/Data::AMF::Packet.3pm*
%doc %{_mandir}/man3/Data::AMF::Parser.3pm*
%doc %{_mandir}/man3/Data::AMF::Parser::AMF0.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/AMF.pm
%{perl_vendorlib}/Data/AMF/Formatter.pm
%{perl_vendorlib}/Data/AMF/Formatter/AMF0.pm
%{perl_vendorlib}/Data/AMF/Header.pm
%{perl_vendorlib}/Data/AMF/IO.pm
%{perl_vendorlib}/Data/AMF/Message.pm
%{perl_vendorlib}/Data/AMF/Packet.pm
%{perl_vendorlib}/Data/AMF/Parser.pm
%{perl_vendorlib}/Data/AMF/Parser/AMF0.pm

%changelog
* Tue May 12 2009 Christoph Maser <cmr@financial.com> - 0.02004-1
- Initial package. (using DAR)
