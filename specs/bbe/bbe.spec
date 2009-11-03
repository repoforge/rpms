# $Id$
# Authority: dag

Summary: Binary block editor
Name: bbe
Version: 0.2.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://members.surfeu.fi/tjsa/bbe/

Source: http://dl.sf.net/bbe-/bbe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The bbe program is a sed-like editor for binary files. bbe performs
basic byte related transformations on blocks of input stream. bbe is
non-interactive command line tool and can be used as a part of a
pipeline. bbe makes only one pass over input stream.

bbe contains also grep-like features, like printing the filename,
offset and block number.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" htmldir="%{_docdir}/%{name}-%{version}"

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/bbe.1*
%doc %{_infodir}/bbe.*
%{_bindir}/bbe

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Initial package. (using DAR)
