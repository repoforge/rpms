# $Id$
# Authority: dag
# Upstream: Jeffrey Thalhammer <thaljef$cpan,org>

### EL6 ships with perl-Perl-Critic-1.105-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Critic

Summary: Critique Perl source code for best-practices
Name: perl-Perl-Critic
Version: 1.117
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Critic/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Critic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(B::Keywords) >= 1.05
BuildRequires: perl(Carp)
BuildRequires: perl(Config::Tiny) >= 2
BuildRequires: perl(English)
BuildRequires: perl(Exception::Class) >= 1.23
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Spec::Unix)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::String)
BuildRequires: perl(List::MoreUtils) >= 0.19
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Pluggable) >= 3.1
BuildRequires: perl(PPI) >= 1.205
BuildRequires: perl(PPI::Document) >= 1.205
BuildRequires: perl(PPI::Document::File) >= 1.205
BuildRequires: perl(PPI::Node) >= 1.205
BuildRequires: perl(PPI::Token::Quote::Single) >= 1.205
BuildRequires: perl(PPI::Token::Whitespace) >= 1.205
BuildRequires: perl(Pod::PlainText)
BuildRequires: perl(Pod::Select)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Readonly) >= 1.03
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::Format) >= 1.13
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(charnames)
BuildRequires: perl(lib)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
Requires: perl(B::Keywords) >= 1.05
Requires: perl(Carp)
Requires: perl(Config::Tiny) >= 2
Requires: perl(English)
Requires: perl(Exception::Class) >= 1.23
Requires: perl(Exporter)
Requires: perl(File::Basename)
Requires: perl(File::Find)
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(File::Spec::Unix)
Requires: perl(File::Temp)
Requires: perl(Getopt::Long)
Requires: perl(IO::String)
Requires: perl(List::MoreUtils) >= 0.19
Requires: perl(List::Util)
Requires: perl(Module::Pluggable) >= 3.1
Requires: perl(PPI) >= 1.205
Requires: perl(PPI::Document) >= 1.205
Requires: perl(PPI::Document::File) >= 1.205
Requires: perl(PPI::Node) >= 1.205
Requires: perl(PPI::Token::Quote::Single) >= 1.205
Requires: perl(PPI::Token::Whitespace) >= 1.205
Requires: perl(Pod::PlainText)
Requires: perl(Pod::Select)
Requires: perl(Pod::Usage)
Requires: perl(Readonly) >= 1.03
Requires: perl(Scalar::Util)
Requires: perl(String::Format) >= 1.13
Requires: perl(base)
Requires: perl(charnames)
Requires: perl(overload)
Requires: perl(strict)
Requires: perl(version)
Requires: perl(warnings)

%filter_from_requires /^perl*/d
%filter_setup

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book Perl
Best Practices. However, Perl::Critic is not limited to PBP and will
even support Policies that contradict Conway. You can enable, disable,
and customize those Polices through the Perl::Critic interface. You can
also create new Policy modules that suit your own tastes.

%package -n perl-Test-Perl-Critic-Policy
Summary:    A framework for testing your custom Policies
Group:      Development/Libraries
License:    GPL+ or Artistic

%description -n perl-Test-Perl-Critic-Policy
This module provides a framework for function-testing your custom
Perl::Critic::Policy modules. Policy testing usually involves feeding it a
string of Perl code and checking its behavior. In the old days, those strings
of Perl code were mixed directly in the test script. That sucked.
%prep
%setup -n %{real_name}-%{version}

# Drop exec bits from samples/docs to avoid dependency bloat
find tools examples -type f -exec chmod -c -x {} ';'

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
%doc Changes INSTALL LICENSE MANIFEST META.yml README TODO.pod examples/
%doc %{_mandir}/man1/perlcritic.1*
%doc %{_mandir}/man3/Perl::Critic.3pm*
%doc %{_mandir}/man3/Perl::Critic::*.3pm*
%doc %{_mandir}/man3/Perl::TODO.3pm*
%{_bindir}/perlcritic
%dir %{perl_vendorlib}/Perl/
%{perl_vendorlib}/Perl/Critic/
%{perl_vendorlib}/Perl/Critic.pm
%{perl_vendorlib}/Perl/TODO.pod

%files -n perl-Test-Perl-Critic-Policy
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Perl::Critic::Policy.3pm*

%changelog
* Thu Apr 19 2012 David Hrbáč <david@hrbac.cz> - 1.117-1
- new upstream release

* Wed Dec 09 2009 Christoph Maser <cmr@financial.com> - 1.105-3
- disable autodeps

* Fri Oct 30 2009 Steve Huff <shuff@vecna.org> - 1.105-2
- Module::Pluggable dependency captured as a BuildRequires, but
  not a Requires; fixed.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.105-1
- Updated to version 1.105.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 1.104-1
- Updated to version 1.104.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.098-1
- Updated to version 1.098.

* Fri Jul 18 2008 Dries Verachtert <dries@ulyssis.org> - 1.082-1
- Fix: perl(Module::Pluggable) requirement added, thanks to Philip Durbin.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.082-1
- Updated to release 1.082.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.080-1
- Updated to release 1.080.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.078-1
- Updated to release 1.078.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.051-1
- Initial package. (using DAR)
