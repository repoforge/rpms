# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Compile

Summary: Compilation based XML processing
Name: perl-XML-Compile
Version: 0.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Compile/

Source: http://search.cpan.org//CPAN/authors/id/M/MA/MARKOV/XML-Compile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Compilation based XML processing.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%doc %{_mandir}/man3/XML::Compile*.3*
%{perl_vendorlib}/XML/Compile.p*
%{perl_vendorlib}/XML/Compile/

%changelog
* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Sat Jan 06 2007 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
