# $Id$
# Authority: dag
# Upstream: Jeffrey Thalhammer <thaljef$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Critic

Summary: Critique Perl source code for best-practices
Name: perl-Perl-Critic
Version: 1.082
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
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.082-1
- Updated to release 1.082.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.080-1
- Updated to release 1.080.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.078-1
- Updated to release 1.078.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.051-1
- Initial package. (using DAR)
