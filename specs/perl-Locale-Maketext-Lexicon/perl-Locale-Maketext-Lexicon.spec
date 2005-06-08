# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#23447;&#28450;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext-Lexicon

Summary: Extract translatable strings from source
Name: perl-Locale-Maketext-Lexicon
Version: 0.49
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext-Lexicon/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/Locale-Maketext-Lexicon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends, 
for "Locale::Maketext" to read from other localization formats, such as 
PO files, MO files, or from databases via the "Tie" interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes README
%doc %{_mandir}/man?/*
%{_bindir}/xgettext.pl
%{perl_vendorlib}/Locale/Maketext

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Updated to release 0.49.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Initial package.
