# $Id$
# Upstream: Ingy dot Net <ingy@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name YAML-Perl

Summary: Pure Perl YAML Implementation
Name: perl-YAML-Perl
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Perl/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Error)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl >= 5.005003
Requires: perl(Error)
Requires: perl(Filter::Util::Call)
Requires: perl >= 5.005003

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/YAML::Perl.3pm*
%doc %{_mandir}/man3/YAML::Perl::Base.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/YAML/Perl.pm
%{perl_vendorlib}/YAML/Perl.pod
%{perl_vendorlib}/YAML/Perl/Base.pm
%{perl_vendorlib}/YAML/Perl/Composer.pm
%{perl_vendorlib}/YAML/Perl/Constructor.pm
%{perl_vendorlib}/YAML/Perl/Dumper.pm
%{perl_vendorlib}/YAML/Perl/Emitter.pm
%{perl_vendorlib}/YAML/Perl/Error.pm
%{perl_vendorlib}/YAML/Perl/Events.pm
%{perl_vendorlib}/YAML/Perl/Loader.pm
%{perl_vendorlib}/YAML/Perl/Nodes.pm
%{perl_vendorlib}/YAML/Perl/Parser.pm
%{perl_vendorlib}/YAML/Perl/Processor.pm
%{perl_vendorlib}/YAML/Perl/Reader.pm
%{perl_vendorlib}/YAML/Perl/Representer.pm
%{perl_vendorlib}/YAML/Perl/Resolver.pm
%{perl_vendorlib}/YAML/Perl/Scanner.pm
%{perl_vendorlib}/YAML/Perl/Serializer.pm
%{perl_vendorlib}/YAML/Perl/Stream.pm
%{perl_vendorlib}/YAML/Perl/Tokens.pm
%{perl_vendorlib}/YAML/Perl/Writer.pm
%exclude %{perl_vendorarch}/auto/*/*/.packlist


%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.02-1
- initial package
