# $Id$
# Authority: dag
# Upstream: Jeffrey Thalhammer <thaljef$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Critic

Summary: Critique Perl source code for best-practices
Name: perl-Perl-Critic
Version: 1.098
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Critic/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Critic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(B::Keywords)
BuildRequires: perl(Test::More)
BuildRequires: perl(Config::Tiny) >= 2
BuildRequires: perl(Exception::Class) >= 1.23
BuildRequires: perl(IO::String)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Pluggable) >= 3.1
BuildRequires: perl(PPI) >= 1.203
BuildRequires: perl(Readonly) >= 1.03
BuildRequires: perl(String::Format) >= 1.13 
BuildRequires: perl(version)

Requires: perl
Requires: perl(B::Keywords)
Requires: perl(Test::More)
Requires: perl(Config::Tiny) >= 2
Requires: perl(Exception::Class) >= 1.23
Requires: perl(IO::String)
Requires: perl(List::MoreUtils)
Requires: perl(Module::Pluggable) >= 3.1
Requires: perl(PPI) >= 1.203
Requires: perl(Readonly) >= 1.03
Requires: perl(String::Format) >= 1.13
Requires: perl(version)

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
