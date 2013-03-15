%define		_class		Net
%define		_subclass	UserAgent
%define		upstream_name	%{_class}_%{_subclass}_Mobile

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	6
Summary:	HTTP mobile user agent string parser
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_UserAgent_Mobile/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Net_UserAgent_Mobile parses HTTP_USER_AGENT strings of (mainly
Japanese) mobile HTTP user agents. It'll be useful in page dispatching
by user agents. This package was ported from Perl's HTTP::MobileAgent.
See http://search.cpan.org/search?mode=module&query=HTTP-MobileAgent.
The author of the HTTP::MobileAgent module is Tatsuhiko Miyagawa.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2012.0
+ Revision: 742168
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4
+ Revision: 679537
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdv2011.0
+ Revision: 613741
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-2mdv2010.1
+ Revision: 468726
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 450229
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.30.0-4mdv2010.0
+ Revision: 441495
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-3mdv2009.1
+ Revision: 322504
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-2mdv2009.0
+ Revision: 237014
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.30.0-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-1mdv2008.0
+ Revision: 15716
- 0.30.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.26.0-1mdv2007.0
+ Revision: 82433
- Import php-pear-Net_UserAgent_Mobile

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.26.0-1mdk
- 0.26.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-1mdk
- initial Mandriva package (PLD import)

