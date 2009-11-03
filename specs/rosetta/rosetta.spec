# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Interactive tool to help translate documents in the DocBook format
Name: rosetta
Version: 0.01
Release: 2.2%{?dist}
License: GPL
Group: Applications/Editors
URL: http://www.irule.be/bvh/c++/rosetta/

Source: http://www.irule.be/bvh/c++/rosetta/rosetta-0.01.tar.gz
Patch0: rosetta-rh8.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++

%description
Rosetta is an interactive tool to help translate documents in the DocBook
format. More specifically it'll read any text with DocBook XML markup and
present it to the translater split-up between mark up and real text. With
appropriate visual feedback it's easy to spot untranslated text. Finally
Rosetta generates a new DocBook document for further processing with the
same structure as the original, but with translated texts.

Rosetta also keeps a dictionary of previously translated sentences. When
an slightly changed version of the original document is read, unchanged
texts is translated directly from the dictionary, greatly reducing the
work to keep the translation up to date with regards to the original.

%prep
%setup
#if %{?rh8:1}%{!?rh8:0}
%patch0 -p1 -b .rh8
#endif
#if %{?rh9:1}%{!?rh9:0}
#patch0 -p1 -b .rh8
#endif

%build
source "%{_sysconfdir}/profile.d/qt.sh"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rosetta %{buildroot}%{_bindir}/rosetta

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR CHANGELOG README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-2.2
- Rebuild for Fedora Core 5.

* Fri Jan  3 2003 Ivo Clarysse <soggie@soti.org> - 0.01-2
- Patched to build on rh8

* Tue Dec 31 2002 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
