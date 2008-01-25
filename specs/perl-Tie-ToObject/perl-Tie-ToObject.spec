# $Id$
# Authority: build

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-ToObject

Summary: Perl module named Tie-ToObject
Name: perl-Tie-ToObject
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-ToObject/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-ToObject-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
While "tie" in perldoc allows tying to an arbitrary object, the class in 
question must support this in it's implementation of TIEHASH, 
TIEARRAY or whatever.

This class provides a very tie constructor that simply returns the object 
it was given as it's first argument.

This way side effects of calling $object->TIEHASH are avoided.

This is used in Data::Visitor in order to tie a variable to an already existing 
object. This is also useful for cloning, when you want to clone the internal state 
object instead of going through the tie interface for that variable.

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
%doc MANIFEST MANIFEST.SKIP META.yml SIGNATURE
%doc %{_mandir}/man3/Tie::ToObject.3pm*
%dir %{perl_vendorlib}/Tie/
#%{perl_vendorlib}/Tie/ToObject/
%{perl_vendorlib}/Tie/ToObject.pm

%changelog
* Fri Jan 25 2008 Quien Sabe <quien-sabe@metaorg.com> - 0.03-1
- Initial package. (using DAR)
