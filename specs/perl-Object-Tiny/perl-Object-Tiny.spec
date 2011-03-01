# $Id$
# Authority: shuff
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Tiny

Summary: Class building as simple as it gets
Name: perl-Object-Tiny
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Tiny/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Object-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: rpm-macros-rpmforge
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
There's a whole bunch of class builders out there. In fact, creating a class
builder seems to be something of a rite of passage (this is my fifth, at
least).

Unfortunately, most of the time I want a class builder I'm in a hurry and
sketching out lots of fairly simple data classes with fairly simple structure,
mostly just read-only accessors, and that's about it.

Often this is for code that won't end up on CPAN, so adding a small dependency
doesn't matter much. I just want to be able to define these classes FAST.

By which I mean LESS typing than writing them by hand, not more. And I don't
need all those weird complex features that bloat out the code and take over the
whole way I build modules.

And so, I present yet another member of the Tiny family of modules,
Object::Tiny.



%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Object/Tiny.pm
#%{perl_vendorlib}/Object/Tiny/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Mar 01 2011 Steve Huff <shuff@vecna.org> - 1.06-1
- Initial package.
