# $Id$
# Authority: dag

Summary: Tool for controlling the special features of a "U3 smart drive" USB Flash disk
Name: u3-tool
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://u3-tool.sourceforge.net/

Source: http://dl.sf.net/project/u3-tool/u3-tool/%{version}/u3-tool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
u3-tool is a tool for controlling the special features of a "U3 smart drive"
USB Flash disk.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/u3-tool.1*
%{_sbindir}/u3-tool

%changelog
* Mon Aug 16 2010 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
