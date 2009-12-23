# $Id$
# Authority: dag
# Upstream: Chris Thompson <cthom$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-Any

Summary: Wrapper Class for the various JSON classes
Name: perl-JSON-Any
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-Any/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PERIGRIN/JSON-Any-1.22.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl-JSON-Any-alternative = %{version}
Requires: perl(Carp)

# don't install without at least one JSON module
Requires: perl-JSON-Any-alternative = %{version}

%filter_from_requires /^perl*/d
%filter_setup


%description
Wrapper Class for the various JSON classes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/JSON::Any.3pm*
%dir %{perl_vendorlib}/JSON/
#%{perl_vendorlib}/JSON/Any/
%{perl_vendorlib}/JSON/Any.pm

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.21-1
- Updated to version 1.21.

* Fri Jun 12 2009 Steve Huff <shuff@vecna.org> - 1.19-2
- Added dependency on perl-JSON-Any-alternative.
- JSON::PC no longer a supported module; removed dependency.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to release 1.19.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
