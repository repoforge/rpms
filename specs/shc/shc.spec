# $Id$
# Authority: dag
# Upstream: Francisco Rosales <frosal$fi,upm,es>

Summary: Generic shell script compiler
Name: shc
Version: 3.8.6
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://www.datsi.fi.upm.es/~frosal/sources/shc.html

Source: http://www.datsi.fi.upm.es/~frosal/sources/shc-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
shc creates a stripped binary executable version a shell script.

shc itself is not a compiler such as cc, it rather encodes and encrypts
a shell script and generates C source code with the added expiration
capability. It then uses the system compiler to compile a stripped
binary which behaves exactly like the original script.

shc's main purpose is to protect your shell scripts from modification
or inspection. You can use it if you wish to distribute your scripts
but don't want them to be easily readable by other people.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 shc %{buildroot}%{_bindir}/shc
%{__install} -Dp -m0755 shc.1 %{buildroot}%{_mandir}/man1/shc.1
#echo "y" | %{__make} install INSTALL_PATH="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES Copying shc.html *.README test.*
%doc %{_mandir}/man1/shc.1*
%{_bindir}/shc

%changelog
* Fri Sep 22 2006 Dag Wieers <dag@wieers.com> - 3.8.6-1
- Initial package. (using DAR)
