# $Id$

# Authority: dag

Summary: An interactive tool to help translate documents in the DocBook format
Name: rosetta
Version: 0.01
Release: 2
License: GPL
Group: Applications/Editors
URL: http://www.irule.be/bvh/c++/rosetta/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.irule.be/bvh/c++/rosetta/rosetta-0.01.tar.gz
Patch0: rosetta-rh8.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: qt-devel

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
#if %{?rh80:1}%{!?rh80:0}
%patch0 -p1 -b .rh8
#endif
#if %{?rh90:1}%{!?rh90:0}
#patch0 -p1 -b .rh8
#endif

%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 rosetta %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR CHANGELOG README
%{_bindir}/*

%changelog
* Fri Jan  3 2003 Ivo Clarysse <soggie@soti.org> - 0.01-2
- Patched to build on rh8

* Tue Dec 31 2002 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
