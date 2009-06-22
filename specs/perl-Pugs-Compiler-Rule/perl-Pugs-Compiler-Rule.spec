# $Id$
# Authority: dag
# Upstream: The Pugs Team C<< <perl6-compiler@perl.org> >>.

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pugs-Compiler-Rule

Summary: Compiler for Perl 6 regexes
Name: perl-Pugs-Compiler-Rule
Version: 0.37
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pugs-Compiler-Rule/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/Pugs-Compiler-Rule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
Compiler for Perl 6 regexes.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO examples/
%doc %{_mandir}/man1/compile_p6grammar.pl.1*
%doc %{_mandir}/man3/Pugs::*.3pm*
%{_bindir}/compile_p6grammar.pl
%{perl_vendorlib}/Pugs/

%changelog
* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Initial package. (using DAR)
