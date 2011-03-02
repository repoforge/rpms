# $Id$
# Authority: dag
# Upstream: Stevan Little E<lt>stevan,little$iinteractive,comE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Params-Validate

Summary: an extension of Params::Validate for using Moose's types
Name: perl-MooseX-Params-Validate
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Params-Validate/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/MooseX-Params-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Devel::Caller)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.58
BuildRequires: perl(Params::Validate) >= 0.88
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Exception) >= 0.21
#BuildRequires: perl(Test::Fatal) >= 0.001
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
Requires: perl(Carp)
Requires: perl(Devel::Caller)
Requires: perl(Moose) >= 0.58
Requires: perl(Params::Validate) >= 0.88
Requires: perl(Scalar::Util)
Requires: perl(Sub::Exporter)

%filter_from_requires /^perl*/d
%filter_setup

%description
an extension of Params::Validate for using Moose's types.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL LICENSE MANIFEST META.json README SIGNATURE
%doc %{_mandir}/man3/MooseX::Params::Validate.3pm*
%dir %{perl_vendorlib}/MooseX/
%dir %{perl_vendorlib}/MooseX/Params/
%{perl_vendorlib}/MooseX/Params/Validate.pm

%changelog
* Wed Mar 02 2011 Steve Huff <shuff@vecna.org> - 0.16-1
- Updated to version 0.16.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
