# $Id$
# Authority: dries
# Upstream: &#20108;&#21313;&#26085;&#9734;&#40736; - IKEDA Soji <hatuka$nezumi,nu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-EncWords

Summary: Deal with RFC-1522 encoded words
Name: perl-MIME-EncWords
Version: 0.040
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-EncWords/

Source: http://search.cpan.org//CPAN/authors/id/N/NE/NEZUMI/MIME-EncWords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Deal with RFC-1522 encoded words.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/MIME::EncWords*
%{perl_vendorlib}/MIME/EncWords.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.040-1
- Initial package.
