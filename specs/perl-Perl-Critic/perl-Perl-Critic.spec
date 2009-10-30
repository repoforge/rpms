# $Id$
# Authority: dag
# Upstream: Jeffrey Thalhammer <thaljef$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Critic

Summary: Critique Perl source code for best-practices
Name: perl-Perl-Critic
Version: 1.105
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Critic/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Critic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(Test::More)
BuildRequires: perl(lib)
# From yaml requires
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
BuildRequires: perl(base)
BuildRequires: perl(charnames)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
# From yaml recommends
BuildRequires: perl(Email::Address)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Which)
BuildRequires: perl(IPC::Open2)
BuildRequires: perl(Perl::Tidy)
BuildRequires: perl(Pod::Spell)
BuildRequires: perl(Readonly::XS)
BuildRequires: perl(Regexp::Parser)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Text::ParseWords)
Requires: perl(Module::Pluggable) >= 3.1

%description
Critique Perl source code for best-practices.

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

%changelog
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
